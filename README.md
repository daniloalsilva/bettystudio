# Betty Studio

Website mobile-first do Betty Studio.

## Desenvolvimento

```bash
make test
python3 -m http.server 4173 --directory _site
```

Cada merge em `main` publica um preview versionado e cria uma release draft. Publicar essa release promove exatamente o artefato validado para produção.
