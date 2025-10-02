export default {
  expo: {
    name: "ADHDers Social Club",
    slug: "adhders-social-club",
    version: "1.0.1",
    owner: "ssaritan",
    platforms: ["ios", "android"],
    android: {
      package: "com.adhders.socialclub",
      versionCode: 3,
    },
    ios: {
      bundleIdentifier: "com.adhders.socialclub",
      buildNumber: "16",
      infoPlist: {
        ITSAppUsesNonExemptEncryption: false,
        GADApplicationIdentifier: "ca-app-pub-8247392015171096~2470722104"
      }
    },
    extra: {
      backendUrl: "https://adhders-social-club.onrender.com",
      ENABLE_ADMOB: false,
      ENABLE_ANIMATIONS: false,
      ENABLE_REANIMATED: false,
      eas: {
        projectId: "48f9e931-8683-4fd8-ac6c-99c5feb158e8"
      }
    }
  }
};
