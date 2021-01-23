set number
set relativenumber
set history=1000 " Store more history
set showcmd      " Show incomplete cmds
set showmode     " Show current mode
set visualbell   " No sound
set hidden       " Allow buffers to be hidden
                 " without writing to the disk
set textwidth=80 " Hard wrap at 80 characters

syntax on        " Turn on syntax highlighting


set autoindent
set smartindent
set smarttab
set shiftwidth=4
set softtabstop=4
set tabstop=4
set expandtab

filetype plugin indent on

" Display whitespace errors as `.'
set list listchars=tab:\ \ ,trail:.

set nowrap    " Do not wrap lines
set linebreak " Wrap lines when convenient

:nmap \p :set paste!<CR>
:nmap j gj
:nmap k gk

call plug#begin('~/.vim/plugged')

Plug 'https://github.com/joshdick/onedark.vim'
Plug 'sheerun/vim-polyglot'
Plug 'drewtempelmeyer/palenight.vim'
Plug 'https://github.com/morhetz/gruvbox'
Plug 'KeitaNakamura/neodark.vim'
Plug 'preservim/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'overcache/NeoSolarized'

call plug#end()

colorscheme gruvbox
"set guifont=Fantasque\ Sans\ Mono\ Regular:h13
set guifont=Fira\ Code\ SemiBold:h13
set background=dark

"Below two lines will enable font ligatures.
"set renderoptions=type:directx
"set encoding=utf-8

"set backup
"set dir=%TMP%
set backupdir=$TMP
set directory=$TMP
set undodir=$TMP
"set noundofile

nmap <F5> :!g++ --std=c++14 -Wall -o %:r.exe %<cr>
nmap <F6> :!%:r.exe<cr>
nmap <F9> :!python %<cr>
nmap <F2> :w<cr>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
