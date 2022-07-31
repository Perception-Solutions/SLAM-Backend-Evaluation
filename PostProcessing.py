from typing import List

import config
from dto.Pcd import Pcd


class PostProcessing:
    """
    Chooses planes with maximum points
    """

    def __get_best_planes(self, pcd_s: List[Pcd]):
        indx_to_max_num_points = {}
        for i, pcd in enumerate(pcd_s):
            print("postprocessing " + str(i))
            for plane in pcd.planes:
                num_of_points = len(plane.plane_indices)
                if (
                    plane.track not in indx_to_max_num_points
                    or num_of_points > indx_to_max_num_points[plane.track]
                ):
                    indx_to_max_num_points[plane.track] = num_of_points
        map_indx_to_max_num_points = sorted(
            indx_to_max_num_points, key=indx_to_max_num_points.get
        )

        return map_indx_to_max_num_points

    def post_process(self, pcd_s: List[Pcd]):
        max_planes = self.__get_best_planes(pcd_s)[-config.MAX_PLANES_COUNT :]

        return max_planes
