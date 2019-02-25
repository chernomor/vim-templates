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
source ~/.vim/templates/templates.vim
```

3. Usage:
```
$ cd ansible/
$ mkdir -p roles/NEWROLE/{tasks,defaults,handlers}
$ vim roles/NEWROLE/tasks/main.yml
$ vim playbooks/NEWPLAYBOOK.yml
```


