from microns_utils import version_utils

__version__ = version_utils.check_package_version(
    package='microns-morphology', 
    check_if_latest=True, 
    check_if_latest_kwargs=dict(
        owner='cajal', 
        repo='microns-morphology', 
        source='tag', 
    )
)

check_latest_version_from_github = version_utils.latest_github_version_checker(owner='cajal', repo='microns-morphology')
