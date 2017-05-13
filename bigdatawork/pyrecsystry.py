from recsys.prediction_algorithms.matrix_factorization import SVD
from recsys.dataset import
reader=
svd=SVD()
svd.load_data(filename='ml-1m/ratings.dat', sep='::', format={'col':0, 'row':1, 'value':2, 'ids': int})
k = 100
svd.compute(k=k, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True, savefile='tmp/movielens')