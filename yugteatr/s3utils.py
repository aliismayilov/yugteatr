from storages.backends.s3boto import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')
# S3BotoStorageReducedRedundancy = lambda: S3BotoStorage(reduced_redundancy=True, location='reduced')
