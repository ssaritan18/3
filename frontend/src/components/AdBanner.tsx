import React from 'react';
import { View, StyleSheet, Platform } from 'react-native';
// AdMob temporarily disabled to fix crash
// import { BannerAd, BannerAdSize } from 'react-native-google-mobile-ads';
import { useSubscription } from '../context/SubscriptionContext';
// import { adMobService } from '../services/AdMobService';

interface AdBannerProps {
  size?: any; // BannerAdSize temporarily disabled
  style?: any;
}

export function AdBanner({ 
  size, 
  style 
}: AdBannerProps) {
  const { subscription } = useSubscription();

  // AdMob temporarily disabled to fix crash
  // Don't show ads for premium users
  if (subscription.tier === 'premium') {
    return null;
  }

  // Return empty view instead of ad
  return (
    <View style={[styles.container, style]}>
      {/* AdMob temporarily disabled to fix crash */}
    </View>
  );
}

export default AdBanner;

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.05)',
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.1)',
    paddingVertical: 4,
  },
});