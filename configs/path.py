from pathlib import Path

PRETRAINED_MODELS_PATH = {
    # models
    'e4e': '/content/StyleHEAT/checkpoints/Encoder_e4e.pth',
    'hfgi': '/content/StyleHEAT/checkpoints/hfgi.pth',
    'stylegan2': '/content/StyleHEAT/checkpoints/StyleGAN_e4e.pth',
    # editing
    'interfacegan': '/content/StyleHEAT/checkpoints/interfacegan_directions/',
    'ganspace': '/content/StyleHEAT/checkpoints/ffhq_pca.pt',
    'FFHQ_PCA': '/content/StyleHEAT/checkpoints/ffhq_PCA.npz',
    '': '',
    # pretrain
    'discriminator': '/content/StyleHEAT/checkpoints/stylegan2_d_256.pth',
    'video_warper': '/content/StyleHEAT/checkpoints/video_warper.pth',
    'styleheat': '/content/StyleHEAT/checkpoints/StyleHEAT_visual.pt',
    # id_loss
    'irse50': '/content/StyleHEAT/checkpoints/model_ir_se50.pth',
    # 3DMM
    'BFM': '/content/StyleHEAT/checkpoints/BFM',
    '3DMM': '/content/StyleHEAT/checkpoints/Deep3D/epoch_20.pth',
}
