package ldbc.snb.datagen.serializer.snb.csv.dynamicserializer.person;

import com.google.common.collect.ImmutableList;
import ldbc.snb.datagen.dictionary.Dictionaries;
import ldbc.snb.datagen.entities.dynamic.person.Person;
import ldbc.snb.datagen.entities.dynamic.relations.Knows;
import ldbc.snb.datagen.entities.dynamic.relations.StudyAt;
import ldbc.snb.datagen.entities.dynamic.relations.WorkAt;
import ldbc.snb.datagen.hadoop.writer.HdfsCsvWriter;
import ldbc.snb.datagen.serializer.DynamicPersonSerializer;
import ldbc.snb.datagen.serializer.snb.csv.CsvSerializer;
import ldbc.snb.datagen.serializer.snb.csv.FileName;

import java.util.Iterator;
import java.util.List;

import static ldbc.snb.datagen.serializer.snb.csv.FileName.*;

public class CsvCompositeMergeForeignDynamicPersonSerializer extends DynamicPersonSerializer<HdfsCsvWriter> implements CsvSerializer {
    @Override
    public List<FileName> getFileNames() {
        return ImmutableList.of(PERSON,PERSON_HAS_INTEREST_TAG,PERSON_WORK_AT,PERSON_STUDY_AT,PERSON_KNOWS_PERSON);
    }

    @Override
    public void writeFileHeaders() {
        writers.get(PERSON).writeHeader(ImmutableList.of("id","firstName","lastName","gender","birthday","creationDate","locationIP","browserUsed","place","language","email"));
        writers.get(PERSON_HAS_INTEREST_TAG).writeHeader(ImmutableList.of("Person.id","Tag.id"));
        writers.get(PERSON_WORK_AT).writeHeader(ImmutableList.of("Person.id","Organisation.id","workFrom"));
        writers.get(PERSON_STUDY_AT).writeHeader(ImmutableList.of("Person.id","Organisation.id","classYear"));
        writers.get(PERSON_KNOWS_PERSON).writeHeader(ImmutableList.of("Person.id","Person.id","creationDate"));
    }

    @Override
    protected void serialize(final Person p) {

        writers.get(PERSON).writeEntry(ImmutableList.of(
                Long.toString(p.accountId()),
                p.firstName(),
                p.lastName(),
                getGender(p.gender()),
                Dictionaries.dates.formatDate(p.birthday()),
                Dictionaries.dates.formatDateTime(p.creationDate()),
                p.ipAddress().toString(),
                Dictionaries.browsers.getName(p.browserId()),
                Integer.toString(p.cityId()),
                buildLanguages(p.languages()),
                buildEmail(p.emails())
                ));

        Iterator<Integer> itInteger = p.interests().iterator();
        while (itInteger.hasNext()) {
            Integer interestIdx = itInteger.next();
            writers.get(PERSON_HAS_INTEREST_TAG).writeEntry(ImmutableList.of(Long.toString(p.accountId()),Integer.toString(interestIdx)));
        }
    }

    @Override
    protected void serialize(final StudyAt studyAt) {
        writers.get(PERSON_STUDY_AT).writeEntry(ImmutableList.of(Long.toString(studyAt.user),Long.toString(studyAt.university),Dictionaries.dates.formatYear(studyAt.year)));
    }

    @Override
    protected void serialize(final WorkAt workAt) {
        writers.get(PERSON_WORK_AT).writeEntry(ImmutableList.of(Long.toString(workAt.user), Long.toString(workAt.company), Dictionaries.dates.formatYear(workAt.year)));
    }

    @Override
    protected void serialize(final Person p, Knows knows) {
        writers.get(PERSON_KNOWS_PERSON).writeEntry(ImmutableList.of(Long.toString(p.accountId()),Long.toString(knows.to().accountId()),Dictionaries.dates.formatDateTime(knows.creationDate())));
    }

}
