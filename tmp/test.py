apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: build-and-deploy
spec:
  params:
    - description: name of the deployment to be patched
      name: deployment-namex
      type: string
    - description: url of the git repo for the code of deployment
      name: git-url
      type: string
    - default: master
      description: revision to be used from repo of the code for deployment
      name: git-revision
      type: string
    - description: image to be build from the code
      name: IMAGE
      type: string
  tasks:
    - name: fetch-repository
      params:
        - name: url
          value: $(params.git-url)
        - name: subdirectory
          value: ''
        - name: deleteExisting
          value: 'true'
        - name: revision
          value: $(params.git-revision)
      taskRef:
        kind: ClusterTask
        name: git-clone
      workspaces:
        - name: output
          workspace: shared-workspace
    - name: build-image
      params:
        - name: IMAGE
          value: $(params.IMAGE)
      runAfter:
        - fetch-repository
      taskRef:
        kind: ClusterTask
        name: buildah
      workspaces:
        - name: source
          workspace: shared-workspace
  workspaces:
    - name: shared-workspace