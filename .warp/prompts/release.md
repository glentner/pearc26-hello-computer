# Release

Create a new GitHub release for this repository.

## Instructions

1. Verify the current branch is `main`. If not, abort and inform the user they should merge their work to `main` first.

2. Fetch the latest tags and determine the most recent version tag:
   ```bash
   git fetch --tags
   git describe --tags --abbrev=0
   ```

3. Suggest the next version number based on semver (ask the user to confirm or provide their preferred version).

4. Create and push the new tag:
   ```bash
   git tag <version>
   git push origin <version>
   ```

5. Create the GitHub release using the `gh` CLI:
   ```bash
   gh release create <version> --title "<version>" --generate-notes
   ```

6. Confirm the release was created and the PDF build workflow was triggered.

## Notes

- The `release_pdf.yml` workflow only triggers on `release: types: [published]`, not on tag pushes
- Tags can be created freely without triggering builds; only explicit releases trigger the PDF build
- Use `--generate-notes` to auto-generate release notes from commits since the last release
