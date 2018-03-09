from typing import List

from external.csv_reader import CSVReader
from external.snapshot_converter import SnapshotConverter
from models.snapshot import Snapshot
from models.statistics import Statistics


class StatisticsSerializer(object):

    @classmethod
    def load(cls, file: str) -> Statistics:
        data = CSVReader.read(filename=file)
        snapshots: List[Snapshot] = []
        for i in range(len(data)):
            if i == 0:
                continue

            snapshot = SnapshotConverter.load(data[i])
            snapshots.append(snapshot)

        return cls._to_statistics(snapshots=snapshots)

    @classmethod
    def _to_statistics(cls, snapshots: List[Snapshot]) -> Statistics:
        power = []
        h_dop = []
        v_dop = []
        t_dop = []
        m_lat = []
        m_long = []
        m_height = []
        m_x = []
        m_y = []
        m_z = []
        s_lat = []
        s_long = []
        s_height = []
        s_x = []
        s_y = []
        s_z = []

        for snap in snapshots:
            power.append(snap.power)
            h_dop.append(snap.h_dop)
            v_dop.append(snap.v_dop)
            t_dop.append(snap.t_dop)
            m_lat.append(snap.m_lat)
            m_long.append(snap.m_long)
            m_height.append(snap.m_height)
            m_x.append(snap.m_x)
            m_y.append(snap.m_y)
            m_z.append(snap.m_z)
            s_lat.append(snap.s_lat)
            s_long.append(snap.s_long)
            s_height.append(snap.s_height)
            s_x.append(snap.s_x)
            s_y.append(snap.s_y)
            s_z.append(snap.s_z)

        return Statistics(power=power, h_dop=h_dop, v_dop=v_dop, t_dop=t_dop,
                          m_lat=m_lat, m_long=m_long, m_height=m_height, m_x=m_x, m_y=m_y, m_z=m_z,
                          s_lat=s_lat, s_long=s_long, s_height=s_height, s_x=s_x, s_y=s_y, s_z=s_z)
