import logging
import settings


def main():
    logging.basicConfig(format='%(asctime)s:(%(levelname)s) %(message)s',
                        filename='mangement_log.log',
                        encoding='utf-8',
                        level=logging.INFO)
    print(settings.project_version)


if __name__ == '__main__':
    main()
