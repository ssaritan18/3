import { StatusBar } from 'expo-status-bar';
import { useEffect, useState } from 'react';
import { View, Text, Image, StyleSheet, ActivityIndicator, TouchableOpacity, Linking } from 'react-native';
import axios from 'axios';
import Constants from 'expo-constants';

const BACKEND_URL = 'https://kanka-hello.preview.emergentagent.com';
const API = `${BACKEND_URL}/api`;

export default function App() {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(true);

  const helloWorldApi = async () => {
    try {
      const response = await axios.get(`${API}/`);
      console.log('API Response:', response.data.message);
      setMessage(response.data.message);
    } catch (e) {
      console.error('API Error:', e);
      setMessage('API connection failed');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    helloWorldApi();
  }, []);

  const openWebsite = () => {
    Linking.openURL('https://emergent.sh');
  };

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      
      <TouchableOpacity onPress={openWebsite}>
        <Image
          source={{ uri: 'https://avatars.githubusercontent.com/in/1201222?s=120&u=2686cf91179bbafbc7a71bfbc43004cf9ae1acea&v=4' }}
          style={styles.logo}
        />
      </TouchableOpacity>
      
      <Text style={styles.title}>Building something incredible ~!</Text>
      
      {loading ? (
        <ActivityIndicator size="large" color="#61dafb" style={styles.loader} />
      ) : (
        <View style={styles.messageContainer}>
          <Text style={styles.messageLabel}>API Response:</Text>
          <Text style={styles.message}>{message}</Text>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f0f10',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  logo: {
    width: 120,
    height: 120,
    marginBottom: 20,
    borderRadius: 60,
  },
  title: {
    fontSize: 20,
    color: '#ffffff',
    marginTop: 20,
    textAlign: 'center',
  },
  loader: {
    marginTop: 30,
  },
  messageContainer: {
    marginTop: 30,
    padding: 15,
    backgroundColor: '#1a1a1b',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#61dafb',
  },
  messageLabel: {
    color: '#61dafb',
    fontSize: 14,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  message: {
    color: '#ffffff',
    fontSize: 16,
  },
});
