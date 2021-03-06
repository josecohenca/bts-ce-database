"""Create cm data format schemas for Huawesi

Revision ID: 41c8d1841d45
Revises: 9bbf9888ebb4
Create Date: 2018-03-28 03:08:11.070000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41c8d1841d45'
down_revision = '9bbf9888ebb4'
branch_labels = None
depends_on = None


def upgrade():

    # Huawei
    op.execute("CREATE SCHEMA huawei_gexport_gsm")
    op.execute("CREATE SCHEMA huawei_gexport_wcdma")
    op.execute("CREATE SCHEMA huawei_gexport_lte")
    op.execute("CREATE SCHEMA huawei_gexport_cdma")
    op.execute("CREATE SCHEMA huawei_gexport_sran")
    op.execute("CREATE SCHEMA huawei_gexport_other")

    op.execute("CREATE SCHEMA huawei_nbi_gsm")
    op.execute("CREATE SCHEMA huawei_nbi_umts")
    op.execute("CREATE SCHEMA huawei_nbi_lte")
    op.execute("CREATE SCHEMA huawei_nbi_cdma")
    op.execute("CREATE SCHEMA huawei_nbi_sran")
    op.execute("CREATE SCHEMA huawei_nbi_other")

    op.execute("CREATE SCHEMA huawei_mml_gsm")
    op.execute("CREATE SCHEMA huawei_mml_umts")
    op.execute("CREATE SCHEMA huawei_mml_lte")
    op.execute("CREATE SCHEMA huawei_mml_cdma")
    op.execute("CREATE SCHEMA huawei_mml_sran")
    op.execute("CREATE SCHEMA huawei_mml_other")

    op.execute("CREATE SCHEMA huawei_cfgsyn")





def downgrade():
    op.execute("DROP SCHEMA huawei_gexport_gsm")
    op.execute("DROP SCHEMA huawei_gexport_wcdma")
    op.execute("DROP SCHEMA huawei_gexport_lte")
    op.execute("DROP SCHEMA huawei_gexport_cdma")
    op.execute("DROP SCHEMA huawei_gexport_sran")
    op.execute("DROP SCHEMA huawei_gexport_other")

    op.execute("DROP SCHEMA huawei_nbi_gsm")
    op.execute("DROP SCHEMA huawei_nbi_umts")
    op.execute("DROP SCHEMA huawei_nbi_lte")
    op.execute("DROP SCHEMA huawei_nbi_cdma")
    op.execute("DROP SCHEMA huawei_nbi_sran")
    op.execute("DROP SCHEMA huawei_nbi_other")

    op.execute("DROP SCHEMA huawei_mml_gsm")
    op.execute("DROP SCHEMA huawei_mml_umts")
    op.execute("DROP SCHEMA huawei_mml_lte")
    op.execute("DROP SCHEMA huawei_mml_cdma")
    op.execute("DROP SCHEMA huawei_mml_sran")
    op.execute("DROP SCHEMA huawei_mml_other")

    op.execute("DROP SCHEMA huawei_cfgsyn")



