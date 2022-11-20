Commands:
	git init - iniciar um novo repositório
	git status - varrer o que foi modificado, adicionado, removido
	git add -A - pega todos os arquivos untracked
	git commit -m "MESSAGE HERE"
	git log - exibe a lista de todos os commits daquele branch
	git branch - vai listar todos os branches que temos no projeto e o que estiver com * é o branch que estamos
	git reset --(soft, mixed or hard) commitCode
		--soft - volta para a versão anterior e com as modificações atuais não commitadas.
		--hard vai ignorar tudo que existia nas outras versões mais atuais (pouco recomendado quando o trabalho é em equipe)
	git checkout - mudar de branch
		Posso usar git checkout HEAD --nomearquivo para voltar com um arquivo
	git diff - mostra o que foi modificado em cada arquivo
	git diff --name-only - mostra o nome do arquivo modificado
	git remote -v
		fetch - puxar alterações (Remoto -> Local)
		push - inserir alterações (Local -> Remoto)
	git revert --no-edit - O que você alterou nesse commit serão desalteradas
		Você ainda tem acesso a aquele commit que fez errado
	git push origin :branchname
		deletar branch remotos
	git branch -D branchname
		deletar branch local	
	git pull (Remoto -> Local)
	
Branch: versão diferentes do seu sistema
	A versão principal do seu sistema se chama master
	Com as branchs dá para separar o sistema em 2 ou mais.
		Mantém a versão principal e começa a trabalhar na v2.0
	HEAD é o branch local
Commit: Quando faz alterações no git. Git salva apenas as modificações feitas

Diferença entre o que está commitado e o que está no seu computador?
Com o git status você vê o que foi modificado e adicionado, mas você não ve o que foi modificado em cada arquivo

Ignorar/Ocultar determinados arquivos -> .gitignore

Fork -> Para contribuir como terceiro em um projeto
