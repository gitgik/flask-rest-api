pkg_origin=gitgik
pkg_name=flask-rest-api
pkg_version=1.0.1
pkg_maintainer="jeegiks@gmail.com"
pkg_upstream_url="https://github.com/gitgik/flask-rest-api"
pkg_exports=([port]=listening_port [database_uri]=database_uri [secret]=secret)
pkg_exposes=(port secret database_uri)
pkg_deps=(core/python)
pkg_build_deps=(core/virtualenv)
pkg_interpreters=(bin/python3.6)

do_verify () {
  return 0
}

do_clean() {
  return 0
}

do_unpack() {
  # copy the contents of the source directory to the habitat cache path
  PROJECT_ROOT="${PLAN_CONTEXT}/.."

  mkdir -p $pkg_prefix
  build_line "Copying project data to $pkg_prefix/"
  cp -r $PROJECT_ROOT/app $pkg_prefix/
  cp -r $PROJECT_ROOT/*.py $pkg_prefix/
  cp -r $PROJECT_ROOT/requirements.txt $pkg_prefix/
  build_line "Copying .env file with preset variables..."
  cp -vr $PROJECT_ROOT/.env $pkg_prefix/
  cp -vr $PROJECT_ROOT/instance $pkg_prefix/
}

do_build() {
  return 0
}

do_install() {
  cd $pkg_prefix
  build_line "Creating virtual environment..."
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
}
