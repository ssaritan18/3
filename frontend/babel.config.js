module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: [
      // Worklets plugin sadece native platformlarda çalışır
      process.env.EXPO_PLATFORM !== 'web' && 'react-native-worklets/plugin',
    ].filter(Boolean),
  };
};