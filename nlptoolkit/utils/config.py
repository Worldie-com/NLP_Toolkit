#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:01:31 2019

@author: weetee
"""

class Config(object):
    def __init__(self, task):
        if task == 'classification':
            self.train_data = "./data/train.csv"
            self.infer_data = "./data/infer.csv"
            self.max_vocab_len = 7000
            self.hidden_size_1 = 330
            self.hidden_size_2 =130
            self.tokens_length = 200
            self.num_classes = 5
            self.train_test_split = 0
            self.test_ratio = 0.1
            self.batch_size = 32
            self.gradient_acc_steps = 1
            self.max_norm = 1.0
            self.num_epochs = 40
            self.lr = 0.001
            self.model_no = 2
            self.train = 1
            self.infer = 0
            
        elif task == 'translation':
            self.src_path = "./data/translation//eng_zh/news-commentary-v13.zh-en.en"
            self.trg_path = "./data/translation/eng_zh/news-commentary-v13.zh-en.zh"
            self.src_lang = "en"
            self.trg_lang = "zh"
            self.batch_size = 16
            self.d_model = 512
            self.ff_dim = 2048
            self.num = 6
            self.n_heads = 8
            self.max_encoder_len = 200
            self.max_decoder_len = 200
            self.num_epochs = 500
            self.lr = 0.0001
            self.gradient_acc_steps = 2
            self.max_norm = 1.0
            self.model_no = 0
            self.train = 1
            self.evaluate = 0
            self.infer = 0
        
        elif task == 'punctuation_restoration':
            self.data_path = "./data/train.tags.en-fr.en"
            self.level = "bpe"
            self.bpe_word_ratio = 0.7
            self.bpe_vocab_size = 7000
            self.batch_size = 32
            self.d_model = 512
            self.ff_dim = 2048
            self.num = 6
            self.n_heads = 8
            self.max_encoder_len = 200
            self.max_decoder_len = 200
            self.LAS_embed_dim = 512
            self.LAS_hidden_size = 512
            self.num_epochs = 500
            self.lr = 0.0003
            self.gradient_acc_steps = 2
            self.max_norm = 1.0
            self.T_max = 5000
            self.model_no = 0
            self.train = 1
            self.infer = 0
        
        elif task == 'summarization':
            self.data_path = "./data/train.tags.en-fr.en"
            self.level = "bpe"
            self.bpe_word_ratio = 0.7
            self.bpe_vocab_size = 7000
            self.max_features_length = 200
            self.d_model = 512
            self.ff_dim = 2048
            self.num = 6
            self.n_heads = 8
            self.max_encoder_len = 200
            self.max_decoder_len = 200
            self.LAS_embed_dim = 512
            self.LAS_hidden_size = 512
            self.batch_size = 32
            self.num_epochs = 500
            self.lr = 0.0003
            self.gradient_acc_steps = 2
            self.max_norm = 1.0
            self.model_no = 0
            self.train = 1
            self.infer = 0
        
        elif task == 'ner':
            self.train_path = "./data/ner/conll2003/eng.train.txt"
            self.test_path = "./data/ner/conll2003/eng.testa.txt"
            self.num_classes = 9
            self.batch_size = 8
            self.tokens_length = 128
            self.max_steps = -1
            self.warmup_steps = 0
            self.weight_decay = 0.0
            self.adam_epsilon = 1e-8
            self.gradient_acc_steps = 1
            self.max_norm = 1.0
            self.num_epochs = 7
            self.lr = 5e-5
            self.model_no = 0
            self.model_type = 'bert'
            self.train = 0
            self.infer = 1
        
        elif task == 'pos':
            self.train_path = "./data/pos/twpos-data-v0.3/full_data/combined.txt"
            self.test_path = "./data/ner/conll2003/eng.testa.txt"
            self.num_classes = 9
            self.batch_size = 8
            self.tokens_length = 128
            self.max_steps = -1
            self.warmup_steps = 0
            self.weight_decay = 0.0
            self.adam_epsilon = 1e-8
            self.gradient_acc_steps = 1
            self.max_norm = 1.0
            self.num_epochs = 7
            self.lr = 5e-5
            self.model_no = 0
            self.model_type = 'bert'
            self.train = 0
            self.infer = 1
        
        elif task == 'ASR':
            self.folder = "train-clean-5"
            self.level = "word"
            self.use_lg_mels = 1
            self.use_conv = 1
            self.n_mels = 80
            self.n_mfcc = 13
            self.n_fft = 25
            self.hop_length = 10
            self.max_frame_len = 1000
            self.d_model = 128
            self.ff_dim = 128
            self.num = 6
            self.n_heads = 4
            self.batch_size = 30
            self.num_epochs = 9000
            self.lr = 0.0003
            self.gradient_acc_steps = 4
            self.max_norm = 1.0
            self.model_no = 0
            self.train = 1
            self.infer = 0