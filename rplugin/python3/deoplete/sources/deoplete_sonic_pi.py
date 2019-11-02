import re
from pathlib import Path
from .base import Base


AUDIO_FORMATS = ['flac', 'wav']
SYNTH_FORMATS = ['scsyndef']

SAMPLE_DIR = Path('/usr/share/sonic-pi/samples/')
SYNTH_DIR = Path('/usr/share/sonic-pi/synthdefs/compiled/')


class Source(Base):

    def __init__(self, vim):
        super(Source, self).__init__(vim)

        self.name = 'sonic-pi'
        self.mark = '[sonic]'
        self.filetypes = ['ruby']

        self.__synth_pattern = re.compile(
            r'(use_synth|synth|with_synth|set_current_synth)\s+:(.*)'
        )
        self.__fx_pattern = re.compile(r'with_fx\s+:(.*)')
        self.__sample_pattern = re.compile(r'sample\s+:(.*)')
        self.__custom_sample_pattern = re.compile(
            r'sample\s+["\'](.*)["\']\s*,\s*:(.*)'
        )

    def on_init(self, context):
        self.__samples = self.__get_dir_content(SAMPLE_DIR,
                                                AUDIO_FORMATS)
        synth_and_fx = self.__get_dir_content(SYNTH_DIR, SYNTH_FORMATS)

        fx_name_pattern = re.compile(r'sonic-pi-fx_(.*)')
        synth_name_pattern = re.compile(r'sonic-pi-(.*)')
        self.__fxs = []
        self.__synths = []
        for name in synth_and_fx:
            if fx_name_pattern.match(name):
                self.__fxs.append(fx_name_pattern.match(name).group(1))
            elif synth_name_pattern.match(name):
                self.__synths.append(synth_name_pattern.match(name).group(1))

    def __get_dir_content(self, path, suffixes):
        return [f.stem for suff in suffixes
                for f in path.glob(f'*.{suff}')]

    def gather_candidates(self, context):
        sample_match = self.__sample_pattern.search(context['input'])
        if sample_match:
            return self.__samples

        custom_sample_match = self.__custom_sample_pattern.search(context['input'])
        if custom_sample_match:
            custom_dir = Path(custom_sample_match.group(1))
            return self.__get_dir_content(custom_dir.expanduser(),
                                          AUDIO_FORMATS)

        synth_match = self.__synth_pattern.search(context['input'])
        if synth_match:
            return self.__synths

        fx_match = self.__fx_pattern.search(context['input'])
        if fx_match:
            return self.__fxs

        return []
