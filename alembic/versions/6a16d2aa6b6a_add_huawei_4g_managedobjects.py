"""Add Huawei 4G managedobjects

Revision ID: 6a16d2aa6b6a
Revises: 805d9d91ef77
Create Date: 2018-02-13 01:44:09.030000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '6a16d2aa6b6a'
down_revision = '805d9d91ef77'
branch_labels = None
depends_on = None


def upgrade():

    managedobjects = sa.sql.table(
        'managedobjects',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_managedobjects_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('label', sa.String(200)),
        sa.Column('parent_pk', sa.Integer),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )

    op.bulk_insert(managedobjects, [
        {'name': 'ALGODEFAULTPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ANR', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'APPCERT', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'BASEBANDEQM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'BASEBANDEQMBOARDREF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'BCCHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'BFMIMOADAPTIVEPARACFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
        {'name': 'CAMGTCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLACBAR', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLACCESS', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLALGOSWITCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLBF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLBFMIMOPARACFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLCHPWRCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLCSPCPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLCOMPALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLICIC', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLICICMCPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLPCPDCCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLPCPDSCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLPCPDSCHPA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLPCPHICH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDLSCHALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDRXPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDSS', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLDYNACBARALGOPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLHOPARACFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLIDPRDUPT', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLLOWPOWER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLMBMSCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLMCPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLMIMOPARACFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLMLB', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLMLBHO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLMRO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLNOACCESSALMPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLOP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLPCALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLPDCCHALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLPUCCHALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLRACHALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLRACTHD', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLRESEL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLRESELGERAN', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLRESELUTRAN', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLRFSHUTDOWN', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLRICALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLSEL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLSERVICEDIFFCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLSHUTDOWN', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLSIMAP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLSTANDARDQCI', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLULCOMPALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLULICIC', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLULICICMCPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLULPCCOMM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLULPCDEDIC', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CELLULSCHALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CERTCHKTSK', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CERTDEPLOY', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CERTMK', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CERTREQ', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CNOPERATOR', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CNOPERATORHOCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CNOPERATORIPPATH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CNOPERATORSTANDARDQCI', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
        {'name': 'CNOPERATORTA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'COUNTERCHECKPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CPBEARER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CQIADAPTIVECFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CRLPOLICY', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CSFALLBACKBLINDHOCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CSFALLBACKHO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CSFALLBACKPOLICYCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CSPCALGOPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'DEVIP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'DHCPRELAYSWITCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'DIFPRI', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'DISTBASEDHO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'DRX', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'DRXPARAGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'DSCPMAP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'EMC', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBALGOSWITCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBAUTOPOWEROFF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBCIPHERCAP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBCONNSTATETIMER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBFUNCTION', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBINTEGRITYCAP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBMLB', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBPATH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ENODEBSHARINGMODE', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'EPGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ETHPORT', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'EUCELLSECTOREQM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'EUCOSCHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'EUTRANEXTERNALCELL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'EUTRANINTRAFREQNCELL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'FDDRESMODE', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'filefooter', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GERANEXTERNALCELL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GERANINTERFCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GERANNCELL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GERANNFREQGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GERANNFREQGROUPARFCN', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GLOBALPROCSWITCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GTPU', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GTRANSPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'HOMEASCOMM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IKECFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERFREQHOGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERRATCELLSHUTDOWN', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERRATHOCDMA1XRTTGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
        {'name': 'INTERRATHOCDMAHRPDGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
        {'name': 'INTERRATHOCOMM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERRATHOCOMMGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERRATHOGERANGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERRATHOUTRANGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERRATPOLICYCFGGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
        {'name': 'INTRAFREQHOGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTRARATHOCOMM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPGUARD', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPPATH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPRT', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LOCATION', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'MIMOADAPTIVEPARACFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'MMEFEATURECFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'MRO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'NE', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'NODE', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'OMCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PCCHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PDCPROHCPARA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PDSCHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PHICHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PUCCHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PUSCHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PUSCHPARAM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RACHCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RET', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RETDEVICEDATA', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RETSUBUNIT', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RLCPDCPPARAGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RRCCONNSTATETIMER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RRUJOINTCALPARACFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'S1', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'S1INTERFACE', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'S1REESTTIMER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SCTPHOST', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SCTPHOSTREF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SCTPLNK', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SCTPPEER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SCTPPEERREF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SECTOR', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SECTORANTENNAREF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SECTOREQM', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SECTOREQMANTENNAREF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SERVICEIFDLEARFCNGRP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SERVICEIFHOCFGGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SERVICEIRHOCFGGROUP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SIMULOAD', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SRSADAPTIVECFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SRSCFG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'STANDARDQCI', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SUBSESSION_NE', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TACALG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TCEIPMAPPING', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TCPACKCTRLALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TCPACKLIMITALG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TCPMSSCTRL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TDDFRAMEOFFSET', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TDDRESMODESWITCH', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TIMEALIGNMENTTIMER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TOLCALG', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TPEALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TRUSTCERT', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TYPDRBBSR', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UDT', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UDTPARAGRP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UETIMERCONST', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'USERPLANEHOST', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'USERPLANEHOSTREF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'USERPLANEPEER', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'USERPLANEPEERREF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UTRANEXTERNALCELL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UTRANNCELL', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UTRANNFREQ', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'VLANMAP', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'VQMALGO', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'VRF', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'X2', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'X2BLACKWHITELIST', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'X2INTERFACE', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
    ])


def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(2, 3))
