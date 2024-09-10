def get_model_path():
    import os

    path = __file__

    #my_path = os.path.dirname(path)
    my_path = "/home/oddsummer/code/fishregression/src/fishregression/model"
    model_path = os.path.join(my_path, "lr_model.pkl")

    return model_path
