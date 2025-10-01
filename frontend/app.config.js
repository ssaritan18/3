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
      googleMobileAdsAppId: "ca-app-pub-3940256099942544~3347511713"
    },
    ios: {
      bundleIdentifier: "com.adhders.socialclub",
      buildNumber: "3",
      googleMobileAdsAppId: "ca-app-pub-3940256099942544~1458002511",
      infoPlist: {
        ITSAppUsesNonExemptEncryption: false,
        GADApplicationIdentifier: "ca-app-pub-3940256099942544~1458002511",
        NSUserTrackingUsageDescription: "This identifier will be used to deliver personalized ads to you."
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
