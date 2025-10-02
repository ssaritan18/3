module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: [
      // Worklets plugin temporarily disabled to fix crash
      // process.env.EXPO_PLATFORM !== 'web' && 'react-native-worklets/plugin',
    ].filter(Boolean),
  };
};