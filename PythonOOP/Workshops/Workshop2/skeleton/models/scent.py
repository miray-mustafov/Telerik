class Scent:


    LAVENDER = 'lavender'
    VANILLA = 'vanilla'
    ROSE = 'rose'

    allowed_scents = [LAVENDER, VANILLA, ROSE]


    @classmethod
    def check_scent(cls, cur_scent):
        if cur_scent not in cls.allowed_scents:
            raise ValueError('Scent invalid!')
        return cur_scent
