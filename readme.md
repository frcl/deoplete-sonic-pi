# deoplete-sonic-pi

This plugin provides a source for deoplete that can complete

* synth names (as in `use_synth :tb303`)
* fx names (as in `with_fx :wobble`)
* build in samples names (as in `sample :loop_amen`)
* custom sample names with literal path (as in `sample '~/my/sample/dir', :my_sample`)

## TODOs

* [ ] keyword and attribute completion
* [ ] sample names when directory path is a variable
* [ ] completion after `.`

* [ ] build in functions
    * ring, chord, scale
    * sample, sample_duration
    * play, play_pattern, play_pattern_timed
    * range, bools, knit, spread
* [ ] chords and scales
    * major, minor
    * major_pentatonic

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
