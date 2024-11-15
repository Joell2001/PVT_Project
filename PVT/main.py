import Controller.develop as develop
import mode.seeder as seeder

if __name__ == '__main__':
    df = seeder.generate_data_with_scipy(20)
    develop.exportar_a_excel(df)