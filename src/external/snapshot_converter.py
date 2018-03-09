from typing import List

from models.snapshot import Snapshot


class SnapshotConverter(object):

    @staticmethod
    def load(data: List[str]) -> Snapshot:
        power = float(data[0])
        h_dop = float(data[1])
        v_dop = float(data[2])
        t_dop = float(data[3])
        m_lat = float(data[4])
        m_long = float(data[5])
        m_height = float(data[6])
        m_x = float(data[7])
        m_y = float(data[8])
        m_z = float(data[9])
        s_lat = float(data[10])
        s_long = float(data[11])
        s_height = float(data[12])
        s_x = float(data[13])
        s_y = float(data[14])
        s_z = float(data[15])
        return Snapshot(power=power, h_dop=h_dop, v_dop=v_dop, t_dop=t_dop,
                        m_lat=m_lat, m_long=m_long, m_height=m_height, m_x=m_x, m_y=m_y, m_z=m_z,
                        s_lat=s_lat, s_long=s_long, s_height=s_height, s_x=s_x, s_y=s_y, s_z=s_z)
