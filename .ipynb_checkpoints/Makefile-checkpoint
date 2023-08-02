update:
	@nbdev_export
	@git add .
	@git commit -m "File update"
	@git push

setup:
	@pip install nbdev
	@nbdev_install_git_hooks
	@pip install jupyterlab-quarto

init:
	@nbdev_new

start: setup init