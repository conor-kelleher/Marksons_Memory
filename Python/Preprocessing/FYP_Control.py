import entity_extraction
import phrases

textType = "Full"
#textType = "Single"

phrases = phrases.Phrases(textType, 2)
phrases.read_saved_phrases()

#phrases.read_text(['.', ','])

entities = entity_extraction.Entities(textType)
#entities.extract_entities()
entities.read_saved_entities()

#phrases_with_nes = phrases.phrases_with_entities(entities)
#occurrence_tuples = phrases.entity_occurrence_in_phrases_tuples(entities)
phrases.write_to_gephi_file(entities, 1)