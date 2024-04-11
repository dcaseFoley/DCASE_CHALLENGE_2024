wget 'https://storage.googleapis.com/foley_dcase_baseline/g_00935000' -P checkpoint/hifi-gan
wget 'https://storage.googleapis.com/foley_dcase_baseline/hifigan_config.json' -P checkpoint/hifi-gan
wget 'https://storage.googleapis.com/foley_dcase_baseline/bottom_1501.pt' checkpoint/pixelsnail
wget 'https://storage.googleapis.com/foley_dcase_baseline/vqvae_800.pt' checkpoint/vqvae

python inference.py --vqvae_checkpoint checkpoint/vqvae/vqvae_800.pt --pixelsnail_checkpoint checkpoint/pixelsnail/bottom_1501.pt --number_of_synthesized_sound_per_class 2
