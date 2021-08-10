from rubix.rubix_session import RubixSession
from rubix.utils.utils import Utils


class RubixPoint:
    def __init__(self,
                 connection: RubixSession,
                 global_uuid: str = None,
                 ):
        self.ctx = connection
        self.global_uuid = global_uuid

    def get_by_uuid(self,
                    point_uuid: str,
                    ):
        """
        get point by its uuid
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        point_uuid: string
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/uuid/{point_uuid}"

        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)

    def patch_by_uuid(self,
                      point_uuid: str,
                      value: float,
                      priority: int,
                      ):
        """
        write a point value by its uuid
        slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid>
        point_uuid: string
        value: float
        priority: int between 1 and 16
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points_value/uuid/{point_uuid}"
        body = {
            "value": value,
            "priority": priority
        }
        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def patch_by_name(self,
                      network_name: str,
                      device_name: str,
                      point_name: str,
                      value: float,
                      priority: int,
                      ):
        """
        write a point value by its names as in network, device and point names
        slave/<g_uuid>/ps/api/generic/points/name/<network_name>/<device_name>/<point_name>
        network_name: string
        device_name: string
        point_name: string
        value: float
        priority: int between 1 and 16
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/name/{network_name}/{device_name}/{point_name}"
        body = {
            "value": value,
            "priority": priority
        }
        res = self.ctx.connection.patch(url, json=body)
        return Utils.http_response_json(res)

    def get_by_name(self,
                    network_name: str,
                    device_name: str,
                    point_name: str
                    ):
        """
        get a point value names as in network, device and point names
        slave/<g_uuid>/ps/api/generic/points/name/<network_name>/<device_name>/<point_name>
        network_name: string
        device_name: string
        point_name: string
        :return: JSON
        """
        url = f"{self.ctx.url}/slave/{self.global_uuid}/ps/api/generic/points/name/{network_name}/{device_name}/{point_name}"
        res = self.ctx.connection.get(url)
        return Utils.http_response_json(res)