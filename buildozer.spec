[app]
title = Physics Calculator
package.name = physicscalc
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1
requirements = python3,kivy==2.2.1
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.2.1
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[requirements]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.gradle_dependencies = 'androidx.core:core:1.9.0'

[android]
p4a.source_dir = 
p4a.branch = develop
android.accept_sdk_license = True
android.permissions = INTERNET

[buildozer.spec]
