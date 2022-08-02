from typing import Dict
from dataclasses import dataclass, field

from checkov.common.bridgecrew.severities import BcSeverities
from cyclonedx.model.vulnerability import VulnerabilitySeverity
from checkov.common.output.report import CheckType
from cyclonedx.output import SchemaVersion

SCA_CHECKTYPES = [CheckType.SCA_PACKAGE, CheckType.SCA_IMAGE]

PURL_TYPE_MAVEN = "maven"

DEFAULT_CYCLONE_SCHEMA_VERSION = SchemaVersion.V1_4

CYCLONE_SCHEMA_VERSION: Dict[str, str] = {
    "1.4": DEFAULT_CYCLONE_SCHEMA_VERSION,
    "1.3": SchemaVersion.V1_3,
    "1.2": SchemaVersion.V1_2,
    "1.1": SchemaVersion.V1_1,
    "1.0": SchemaVersion.V1_0
}

FILE_NAME_TO_PURL_TYPE = {
    "build.gradle": "maven",
    "build.gradle.kts": PURL_TYPE_MAVEN,
    "composer.json": "composer",
    "Gemfile": "gem",
    "go.mod": "golang",
    "go.sum": "golang",
    "package.json": "npm",
    "package-lock.json": "npm",
    "Pipfile": "pypi",
    "Pipfile.lock": "pypi",
    "pom.xml": "maven",
    "requirements.txt": "pypi",
    "yarn.lock": "npm"
}

IMAGE_DISTRO_TO_PURL_TYPE = {
    'Debian': 'deb',
    'Red': 'rpm',
    'CentOS': 'rpm',
    'Fedora': 'rpm',
    'openSUSE': 'rpm',
    'AlmaLinux': 'rpm',
    'Asianux': 'rpm',
    'ClearOS': 'rpm',
    'Fermi': 'rpm',
    'Miracle': 'rpm',
    'Oracle': 'rpm',
    'Rocky': 'rpm',
    'Scientific': 'rpm',
    'Amazon': 'rpm',
    'SUSE': 'rpm',
    'GeckoLinux': 'rpm',
    'Mandriva': 'rpm',
    'Mageia': 'rpm',
    'ROSA': 'rpm',
    'OpenMandriva': 'rpm',
    'Unity': 'rpm',
    'PCLinuxOS': 'rpm',
    'Vine': 'rpm',
    'ALT': 'rpm',
    'Caldera': 'rpm',
    'cAos': 'rpm',
    'Turbolinux': 'rpm',
    'Astra': 'deb',
    'Bharat': 'deb',
    'Canaima': 'deb',
    'Corel': 'deb',
    'CrunchBang': 'deb',
    'Deepin': 'deb',
    'Devuan': 'deb',
    'Dreamlinux': 'deb',
    'Emdebian': 'deb',
    'Finnix': 'deb',
    'gNewSense': 'deb',
    'Gnoppix': 'deb',
    'grml': 'deb',
    'HandyLinux': 'deb',
    'Kanotix': 'deb',
    'Knoppix': 'deb',
    'Kurumin': 'deb',
    'LEAF': 'deb',
    'LiMux': 'deb',
    'LMDE': 'deb',
    'Maemo': 'deb',
    'MEPIS': 'deb',
    'MintPPC': 'deb',
    'Musix': 'deb',
    'NepaLinux': 'deb',
    'OpenZaurus': 'deb',
    'Pardus': 'deb',
    'PelicanHPC': 'deb',
    'Q4OS': 'deb',
    'Raspberry': 'deb',
    'Sacix': 'deb',
    'Skolelinux': 'deb',
    'Slax (since': 'deb',
    'SolydXK': 'deb',
    'SparkyLinux': 'deb',
    'Sunwah': 'deb',
    'The': 'deb',
    'TurnKey': 'deb',
    'Twister': 'deb',
    'Ubuntu': 'deb',
    'Univention': 'deb',
    'Webconverger': 'deb',
    'Vyatta': 'deb',
    'VyOS': 'deb',
    'BackTrack': 'deb',
    'gLinux': 'deb',
    'Kali': 'deb',
    'Parsix': 'deb',
    'EOL[44]': 'deb',
    'PureOS': 'deb',
    'Parrot': 'deb',
    'antiX': 'deb',
    'MX': 'deb',
    'Damn': 'deb',
    'Feather': 'deb',
    'Hikarunix': 'deb',
    'Kubuntu': 'deb',
    'Lubuntu': 'deb',
    'Xubuntu': 'deb',
    'Edubuntu': 'deb',
    'Gobuntu': 'deb',
    'Mythbuntu': 'deb',
    'BackBox': 'deb',
    'BackSlash': 'deb',
    'Bodhi': 'deb',
    'Cub': 'deb',
    'DNALinux (based': 'deb',
    'dyne:bolic': 'deb',
    'EasyPeasy': 'deb',
    'Eeebuntu': 'deb',
    'Element': 'deb',
    'elementary': 'deb',
    'Emmabuntüs': 'deb',
    'GalliumOS': 'deb',
    'GendBuntu': 'deb',
    'Goobuntu': 'deb',
    'gOS': 'deb',
    'Joli': 'deb',
    'Karoshi': 'deb',
    'KDE': 'deb',
    'Linux': 'deb',
    'LinuxMCE': 'deb',
    'LinuxTLE': 'deb',
    'LliureX': 'deb',
    'LXLE': 'deb',
    'MAX': 'deb',
    'Molinux': 'deb',
    'Netrunner': 'deb',
    'Nova': 'deb',
    'OpenGEU': 'deb',
    'Peppermint': 'deb',
    'Pinguy': 'deb',
    'Pop!': 'deb',
    'Poseidon': 'deb',
    'Sabily': 'deb',
    'Trisquel': 'deb',
    'UberStudent': 'deb',
    'Ututo': 'deb',
    'Vinux': 'deb',
    'Zorin': 'deb'
}

TWISTCLI_PACKAGE_TYPE_TO_PURL_TYPE = {
    'python' : 'pypi',
    'nodejs' : 'npm',
    'jar' : 'maven',
    'rust': 'cargo'
}

BC_SEVERITY_TO_CYCLONEDX_LEVEL = {
    BcSeverities.CRITICAL: VulnerabilitySeverity.CRITICAL,
    BcSeverities.HIGH: VulnerabilitySeverity.HIGH,
    BcSeverities.MEDIUM: VulnerabilitySeverity.MEDIUM,
    BcSeverities.LOW: VulnerabilitySeverity.LOW,
    BcSeverities.NONE: VulnerabilitySeverity.NONE,
}


@dataclass
class ImageDetails:
    distro: str = ''
    distro_release: str = ''
    package_types: dict = field(default_factory=dict)
