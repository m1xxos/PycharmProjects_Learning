class Puppy:
    n_puppies = 0

    # define __new__
    def __new__(cls, *args, **kwargs):
        if Puppy.n_puppies < 10:
            instance = object.__new__(cls)
            cls.n_puppies += 1
            return instance
