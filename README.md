## Installation

1. Clone repo:
```
$ mkdir -p ~/.vim
$ git clone https://github.com/chernomor/vim-templates.git ~/.vim/templates
```
Or add submodule:
```
$ cd ~/.vim/
$ git submodule add https://github.com/chernomor/vim-templates.git templates
```


2. Add to your `.vimrc`:

```
if has("autocmd")
  augroup ansible
    autocmd!

    autocmd BufNewFile playbooks/*.yml   0r ~/.vim/templates/ansible/playbook.yml
    autocmd BufNewFile handlers/main.yml 0r ~/.vim/templates/ansible/handlers-main.yml
    autocmd BufNewFile    tasks/main.yml 0r ~/.vim/templates/ansible/tasks-main.yml
    autocmd BufNewFile defaults/main.yml 0r ~/.vim/templates/ansible/defaults-main.yml
                                                                    
  augroup END                                                       
endif
```

3. Usage:
```
$ cd ansible/
$ mkdir -p roles/NEWROLE/{tasks,defaults,handlers}
$ vim roles/NEWROLE/tasks/main.yml
$ vim playbooks/NEWPLAYBOOK.yml
```


