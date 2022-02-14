import boto3


def handler():

    # the service endpoint of ECRR public must be in `us-east-1`
    client = boto3.client(
        'ecr-public',
        region_name='us-east-1'
    )

    public_repos = client.describe_repositories()['repositories']
    # print(public_repos)

    for repo in public_repos:
        print(repo['repositoryName'])
        images = client.describe_images(repositoryName=repo['repositoryName'])[
            'imageDetails']
        # get the untagged images of the repo
        images_to_delete = [{'imageDigest': image['imageDigest']}
                            for image in images if 'imageTags' not in image.keys()]
        if images_to_delete:
            print(images_to_delete)
            # delete the untagged images
            client.batch_delete_image(
                repositoryName=repo['repositoryName'],
                imageIds=images_to_delete
            )
        else:
            print(f'\t' + 'No images to delete in {repo["repositoryName"]}')


if __name__ == '__main__':
    handler()
