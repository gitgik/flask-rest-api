pkg_origin=gitgik
pkg_name=flask-rest-api
pkg_version=1.0.0
pkg_maintainer="jeegiks@gmail.com"
pkg_upstream_url="https://github.com/gitgik/flask-rest-api"
pkg_exports=([port]=listening_port)
pkg_exposes=(port)
pkg_deps=(core/python)
pkg_build_deps=(core/virtualenv)
pkg_lib_dirs=(lib)
pkg_bin_dirs=(bin)
pkg_include_dirs=(include Include)
pkg_interpreters=(bin/python bin/python3 bin/python3.6)

do_verify () {
  return 0
}

do_clean() {
  return 0
}

do_unpack() {
  # copy the contents of the source directory to the habitat cache path
  cp -vr $PLAN_CONTEXT/../*  $HAB_CACHE_SRC_PATH/$pkg_dirname

  PROJECT_ROOT="${PLAN_CONTEXT}/.."
}

do_build() {
  return 0
}

do_install() {

  # copy the node modules into the package using the pkg_prefix variable
  mkdir -p ${pkg_prefix}/app/
  cp -vr app/* ${pkg_prefix}/app/

  mkdir -p ${pkg_prefix}/instance/
  cp -vr instance/* ${pkg_prefix}/instance/

  cp -vr *.py ${pkg_prefix}/
  cp -vr requirements.txt ${pkg_prefix}/
  cp -vr .env ${pkg_prefix}/

  virtualenv venv

  source .env
  pip install -r requirements.txt
}
