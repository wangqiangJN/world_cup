import argparse

class Hparams:
     parser = argparse.ArgumentParser()

     #path
    # parser.add_argument('save_path', default='/zxgu/wq/rs/model_wq/save/model_ckpt/', type=str)

     #
     parser.add_argument('--hidden_unit', default=225, type=int)
     parser.add_argument('--lr', default=3e-3, type=int)


     #train
     parser.add_argument('--train_batch_size', default=64, type=int)
     parser.add_argument('--predict_batch_size', default=32, type=int)
     parser.add_argument('--predict_users_num', default=1000, type=int)
     parser.add_argument('--predict_ads_num', default=100, type=int)
     parser.add_argument('--random_seed', default=1234, type=int)


     #input
     parser.add_argument('--user_count', default=None, type=int)
     parser.add_argument('--item_count', default=19, type=int)
     parser.add_argument('--time_count', default=86400, type=int)
     parser.add_argument('--speed_count', default=150, type=int)
     parser.add_argument('--lasttime_count', default=150, type=int)

     #auc
     parser.add_argument('--best_auc', default=0.0, type=float)

     



     
