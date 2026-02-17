# Instructions

## Running the App

To run the app, simply run the `main.py` file:

```bash
python main.py
```

## Building the App

To build the app, you need to have `buildozer` installed. You can install it with pip:

```bash
pip install buildozer
```

Once you have `buildozer` installed, you can build the app with the following command:

```bash
buildozer android release
```

This will create a release APK in the `bin` directory.

## Releasing the App

To release the app, you need to create a new release on GitHub. This will trigger the `build-and-release` workflow, which will build the app and upload the APK to the release.
