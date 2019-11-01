# deoplete-sonic-pi

This plugin provides a source for deoplete that can complete

* synth names (as in `use_synth :tb303`)
* fx names (as in `with_fx :wobble`)
* build in samples names (as in `sample :loop_amen`)
* custom sample names (as in `sample '~/my/sample/dir', :my_sample`)

## TODOs

* [ ] keyword and attribute completion
* [ ] completion after `.`

## Requirements and installation

To be able to use this you need

* [neovim](https://github.com/neovim/neovim)
* the neovim [python client](https://github.com/neovim/python-client)
* [deoplete.nvim](https://github.com/Shougo/deoplete.nvim)
* [Sonic Pi](https://sonic-pi.net)

Then just install this plugin with your favorite plugin manager.
For example, I use [minpac](https://github.com/k-takata/minpac):

    # init.vim
    call minpac#add('frcl/deoplete-sonic-pi')

and then `:call minpac#update()`.
