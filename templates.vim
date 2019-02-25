" vim: set expandtab ts=2 sts=2 sw=2:

if has("autocmd")

  augroup ansible
    autocmd!

    " ansible yml
    autocmd BufNewFile playbooks/*.yml   0r ~/.vim/templates/ansible/playbook.yml
    autocmd BufNewFile handlers/main.yml 0r ~/.vim/templates/ansible/handlers-main.yml
    autocmd BufNewFile    tasks/main.yml 0r ~/.vim/templates/ansible/tasks-main.yml
    autocmd BufNewFile defaults/main.yml 0r ~/.vim/templates/ansible/defaults-main.yml

     " RPM.spec
    autocmd BufNewFile *.spec 0r ~/.vim/templates/rpm.spec

  augroup END

endif
