def keyword_param(**param):
    for k, v in param.items():
        print('{} {}'.format(k, v))


map = {1:2, 3:4}
keyword_param(map**)
