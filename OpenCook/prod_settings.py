from .settings from *
import dj_database_url
# 把 debug 模式關掉
DEBUG = False
# 遵守 HTTPS 連線中的連線中的 ”X-Forwarder_Proto" header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDER_PROTO', 'https')
# 設定靜態檔案位置
STATIC_ROOT = 'staticfiles'
#設定資料庫
DATABASES = {
  'default': dj_database_url.config()
}
#允許所有網址連至網站
ALLOWED_HOSTS = ['*']

