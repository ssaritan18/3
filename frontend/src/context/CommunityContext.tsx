import React, { createContext, useCallback, useContext, useEffect, useState } from 'react';
import { Alert } from 'react-native';
import { api, setAuthToken as setApiAuthToken } from '../lib/api';
import { getAuthToken } from '../utils/authTokenHelper';
export type Post = {
  id: string;
  content: string;
  author: string;
  authorId: string;
  category: string;
  timestamp: string;
  likes: number;
  replies: number;
  shares: number;
  userLiked: boolean;
};

type CommunityContextType = {
  posts: Post[];
  loading: boolean;
  error: string | null;
  refreshPosts: () => Promise<void>;
  createPost: (content: string, category?: string) => Promise<void>;
  reactToPost: (postId: string, reactionType?: string) => Promise<void>;
  deletePost: (postId: string) => Promise<void>;
  addComment: (postId: string, text: string) => Promise<void>;
};

const CommunityContext = createContext<CommunityContextType | null>(null);

export function useCommunity() {
  const context = useContext(CommunityContext);
  if (!context) {
    throw new Error('useCommunity must be used within CommunityProvider');
  }
  return context;
}

function normalizePost(input: any): Post {
  return {
    id: input.id || input._id || `post_${Date.now()}`,
    content: input.content || input.text || '',
    author: input.author || input.author_name || 'Anonymous',
    authorId: input.author_id || input.authorId || '',
    category: input.category || 'general',
    timestamp: input.timestamp || input.created_at || new Date().toISOString(),
    likes: typeof input.likes === 'number' ? input.likes : 0,
    replies: typeof input.replies === 'number' ? input.replies : (input.comments_count ?? 0),
    shares: typeof input.shares === 'number' ? input.shares : 0,
    userLiked: Boolean(input.user_liked ?? input.userLiked ?? false),
  };
}

export function CommunityProvider({ children }: { children: React.ReactNode }) {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const ensureToken = useCallback(async () => {
    const token = await getAuthToken();
    if (token) {
      setApiAuthToken(token);
    }
    return token;
  }, []);

  const refreshPosts = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await api.get('/community/posts');
      const data = response.data;

      if (data?.success && Array.isArray(data.posts)) {
        setPosts(data.posts.map(normalizePost));
      } else {
        setPosts([]);
      }
    } catch (err) {
      console.error('Failed to load community posts:', err);
      setError('Failed to load community posts');
    } finally {
      setLoading(false);
    }
  }, []);

  const createPost = useCallback(async (content: string, category = 'general') => {
    if (!content.trim()) {
      return;
    }

    try {
      const token = await ensureToken();
      if (!token) {
        Alert.alert('Authentication Required', 'Please sign in to create posts.');
        return;
      }

      const response = await api.post('/community/posts', { content: content.trim(), category });
      const data = response.data;

      if (data?.success && data.post) {
        setPosts(prev => [normalizePost(data.post), ...prev]);
      } else {
        throw new Error('Invalid response from server');
      }
    } catch (err) {
      console.error('Failed to create community post:', err);
      Alert.alert('Error', 'Failed to create post.');
    }
  }, [ensureToken]);

  const reactToPost = useCallback(async (postId: string, reactionType = 'like') => {
    if (reactionType !== 'like') {
      console.warn('Only like reactions are supported for community posts at this time.');
    }

    try {
      const token = await ensureToken();
      if (!token) {
        Alert.alert('Authentication Required', 'Please sign in to react to posts.');
        return;
      }

      const response = await api.post(`/community/posts/${postId}/like`);
      const data = response.data;

      if (data?.success) {
        setPosts(prev => prev.map(post => post.id === postId
          ? { ...post, userLiked: Boolean(data.liked), likes: typeof data.likes === 'number' ? data.likes : post.likes }
          : post));
      }
    } catch (err) {
      console.error('Failed to react to community post:', err);
      Alert.alert('Error', 'Failed to react to post.');
    }
  }, [ensureToken]);

  const deletePost = useCallback(async (postId: string) => {
    try {
      const token = await ensureToken();
      if (!token) {
        Alert.alert('Authentication Required', 'Please sign in to delete posts.');
        return;
      }

      await api.delete(`/community/posts/${postId}`);
      setPosts(prev => prev.filter(post => post.id !== postId));
    } catch (err) {
      console.error('Failed to delete community post:', err);
      Alert.alert('Error', 'Failed to delete post.');
    }
  }, [ensureToken]);

  const addComment = useCallback(async (postId: string, text: string) => {
    if (!text.trim()) {
      return;
    }

    try {
      const token = await ensureToken();
      if (!token) {
        Alert.alert('Authentication Required', 'Please sign in to reply to posts.');
        return;
      }

      const response = await api.post(`/community/posts/${postId}/reply`, { content: text.trim() });
      const data = response.data;

      if (data?.success) {
        setPosts(prev => prev.map(post => post.id === postId
          ? { ...post, replies: typeof data.replies === 'number' ? data.replies : post.replies }
          : post));
      }
    } catch (err) {
      console.error('Failed to add reply to community post:', err);
      Alert.alert('Error', 'Failed to add reply.');
    }
  }, [ensureToken]);

  useEffect(() => {
    refreshPosts();
  }, [refreshPosts]);

  const value: CommunityContextType = {
    posts,
    loading,
    error,
    refreshPosts,
    createPost,
    reactToPost,
    deletePost,
    addComment,
  };

  return (
    <CommunityContext.Provider value={value}>
      {children}
    </CommunityContext.Provider>
  );
}
