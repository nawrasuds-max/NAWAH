[app]

# اسم التطبيق
title = Physics Calculator

# اسم الحزمة (package name)
package.name = physicscalc

# نطاق الحزمة (package domain)
package.domain = org.example

# المجلد المصدر (حيث يوجد ملف main.py)
source.dir = .

# الملفات المرفوعة
source.include_exts = py,png,jpg,kv,atlas,txt

# الإصدار
version = 0.1

# المتطلبات (مهم جداً!)
requirements = python3,kivy==2.1.0

# اتجاه الشاشة
orientation = portrait

# وضع ملء الشاشة
fullscreen = 0

[buildozer]

# مستوى تسجيل الأخطاء
log_level = 2

# تحذير عند التشغيل كـ root
warn_on_root = 1

[requirements]

# إصدار Android API
android.api = 31

# أقل إصدار Android مدعوم
android.minapi = 21

# إصدار NDK
android.ndk = 25b

# إصدار SDK
android.sdk = 31

# تبعيات Gradle
android.gradle_dependencies = androidx.core:core:1.7.0

[android]

# فرع python-for-android
p4a.branch = develop

# قبول ترخيص SDK
android.accept_sdk_license = True

# أذونات التطبيق
android.permissions = INTERNET
