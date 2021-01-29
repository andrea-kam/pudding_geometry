import numpy as np
from scipy.optimize import fsolve

class Pudding():
    def __init__(self, h, r1, r2):
        self.h = h
        self.r1 = r1
        self.r2 = r2
        print('A PUDDING HAS BEEN BAKED!')
        print(f'Height={h}, upper radius={r1}, lower radius={r2}.')

    @staticmethod
    def eval_cut_factor(cut_dist_ratio):
        return np.arccos(cut_dist_ratio) - cut_dist_ratio * np.sin(np.arccos(cut_dist_ratio))

    def get_cut_factor(self, cut_dist_ratio, prop):
        """ Solve get_cut_factor(u, prop)=0 for the u required to obtain prop of the total pudding volume """
        return self.eval_cut_factor(cut_dist_ratio) - prop

    def get_volume(self, cut_dist_ratio):
        v_tot = self.h / 3 * (self.r2 ** 2 + self.r1 * self.r2 + self.r1 ** 2)
        if cut_dist_ratio==0:
            print(f'Volume of the whole pudding is {v_tot}')
        else:
            cut_factor = self.eval_cut_factor(cut_dist_ratio)
            v = v_tot * cut_factor
            print(f'Volume of the pudding is {v} when cut at a distance ratio of {cut_dist_ratio} from the centre.')

    def find_cut_dist_from_centre(self, v_prop):
        u_solution = fsolve(self.get_cut_factor, 1-v_prop, args=v_prop)
        print(f'Cut across at {u_solution} of the radius from the centre to get {v_prop} of the pudding volume.')

