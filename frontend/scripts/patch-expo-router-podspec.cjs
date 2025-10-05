const fs = require('fs');
const path = require('path');

const podspecPath = path.join(__dirname, '..', 'node_modules', 'expo-router', 'ios', 'ExpoHead.podspec');

function log(message) {
  console.log(`[patch-expo-router] ${message}`);
}

try {
  if (!fs.existsSync(podspecPath)) {
    log(`skipping, missing file: ${podspecPath}`);
    process.exit(0);
  }

  const contents = fs.readFileSync(podspecPath, 'utf8');

  if (contents.includes("'HEADER_SEARCH_PATHS' => '$(inherited)'") && contents.includes('add_dependency(s, "RNScreens")\n')) {
    log('ExpoHead.podspec already patched.');
    process.exit(0);
  }

  const needle = "  s.dependency 'ExpoModulesCore'\n\n  add_dependency(s, \"RNScreens\")\n\n  # Swift/Objective-C compatibility\n  s.pod_target_xcconfig = {\n    'DEFINES_MODULE' => 'YES',\n    'SWIFT_COMPILATION_MODE' => 'wholemodule',\n    'OTHER_SWIFT_FLAGS' => \"$(inherited) #{compiler_flags}\",\n  }";

  if (!contents.includes(needle)) {
    log('Unexpected ExpoHead.podspec contents; manual check required.');
    process.exit(0);
  }

  const replacement = "  s.dependency 'ExpoModulesCore'\n\n  # Swift/Objective-C compatibility\n  s.pod_target_xcconfig = {\n    'DEFINES_MODULE' => 'YES',\n    'SWIFT_COMPILATION_MODE' => 'wholemodule',\n    'OTHER_SWIFT_FLAGS' => \"$(inherited) #{compiler_flags}\",\n    'HEADER_SEARCH_PATHS' => '$(inherited)',\n  }\n\n  add_dependency(s, \"RNScreens\")";

  const updated = contents.replace(needle, replacement);

  if (updated === contents) {
    log('Pattern replacement failed; no changes written.');
    process.exit(0);
  }

  fs.writeFileSync(podspecPath, updated, 'utf8');
  log('Patched ExpoHead.podspec to configure HEADER_SEARCH_PATHS before add_dependency.');
} catch (error) {
  console.warn(`[patch-expo-router] Failed to patch ExpoHead.podspec: ${error.message}`);
  process.exit(0);
}
