export default {
  expo: {
    name: "ADHDers Social Club",
    slug: "adhders-social-club",
    version: "1.0.0",
    android: {
      package: "com.adhders.socialclub"
    },
    ios: {
      bundleIdentifier: "com.adhders.socialclub",
      infoPlist: {
        ITSAppUsesNonExemptEncryption: false
      }
    },
    extra: {
      backendUrl: "https://adhders-social-club.onrender.com",
      eas: {
        projectId: "48f9e931-8683-4fd8-ac6c-99c5feb158e8"
      }
    }
  }
};
