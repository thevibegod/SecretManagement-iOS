import os


def generate_secret_manager(filename: str, directory_path: str):
    api_key_1 = os.environ["API_KEY_1"]
    api_key_2 = os.environ["API_KEY_2"]

    filepath = os.path.join(directory_path, filename)

    with open(filepath, 'w') as f:
        f.write(
            f'''//  AUTOGENERATED USING PYTHON. DO NOT EDIT OR COMMIT THIS FILE.
//
//  {filename}
//

import Foundation

struct SampleAppSecretManager {{
    static let shared: Self = .init()
    let apiKey1: String
    let apiKey2: String

    private init() {{
        self.apiKey1 = "{api_key_1}"
        self.apiKey2 = "{api_key_2}"
    }}
}}''')


if __name__ == '__main__':

    directory_path = "Generated"
    filename = "SampleAppSecretManager.generated.swift"

    generate_secret_manager(filename, directory_path)
