wget 'https://storage.googleapis.com/foley_dcase_baseline/g_00935000' -P checkpoint/hifi-gan
wget 'https://storage.googleapis.com/foley_dcase_baseline/hifigan_config.json' -P checkpoint/hifi-gan
wget 'https://storage.googleapis.com/foley_dcase_baseline/bottom_1501.pt' -P checkpoint/pixelsnail
wget 'https://storage.googleapis.com/foley_dcase_baseline/vqvae_800.pt' -P checkpoint/vqvae
pip install torch==1.13.1 librosa==0.10.0 python-lmdb tqdm

python inference.py --vqvae_checkpoint checkpoint/vqvae/vqvae_800.pt --pixelsnail_checkpoint checkpoint/pixelsnail/bottom_1501.pt --number_of_synthesized_sound_per_class 10
