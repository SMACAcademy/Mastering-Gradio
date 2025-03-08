from transformers import pipeline
summarizer = pipeline("summarization", model="Mahalingam/DistilBart-Med-Summary", device=0,)

conversation = '''This is a 70 y/o male, with a history of DM who underwent left total hip placement on 3/1/16 and has a chronic DM
wound on the left foot. Pt was transferred to SNF for rehab from 3/5-4/5/16. Patient was referred to home health
PT and SN. Patient was evaluated by PT and SN to initiate care on 4/7/16, physician order requesting 7 PT visits
and 4 SN visits in a 60 day period.
Current status from PT:
1. Lives with wife in 2-story house home bound due to stairs and unsteady gait.
2. Ambulates with FFW 15feet with min verbal and tactile cues to decrease distance between self and walker,
managing walker in proper direction and speed.
3. Minimum assist sit to stand from wheelchair
4. Minimum assist transfers
5. Sit to supine: maximum assist
Current Status of wound:
1. Slow healing DM ulcer on left medial metatarsal head, surgically debrided during hospitalization.
Treatment Plan and Goal:
1. Home PT will continue treatment to train patient and care giver on fall prevention, proper body mechanics,
progressive ROM strengthening and balance exercises, HEP, pain management, equipment usage.
2. SN reported bilateral 2+ edema, will teach care giver to wrap and ted hose 2x a week.
3. Promogran Prisma matrix moistened with hydrogel, cover with silver foam and secure with Kerlix to be
changed every 2-3 days. Skilled Nurse will educate wife on dressing changes
4. SN is required to assess wound healing, and monitor for infection
5. Patient’s next WCC visit is 5/20/16.'''

conversation1='''Patient [Patient Name], a 45-year-old office worker, presented with chronic low back pain radiating down the right leg, aggravated by prolonged sitting and lifting. Examination revealed decreased lumbar spine range of motion, positive straight leg raise test on the right, and weakness in the right gluteal muscles. Diagnosis: Lumbar disc herniation with radiculopathy.
Physiotherapy intervention consisted of manual therapy techniques including lumbar spine mobilizations, soft tissue release, and trigger point therapy. Specific strengthening exercises for core muscles and hip flexors were also implemented along with stretches for the hamstrings and lower back. Patient reported significant pain reduction and improved functional ability throughout treatment.
At discharge, patient demonstrated significantly improved lumbar spine range of motion, reduced pain with activities of daily living, and was able to perform strengthening exercises independently. Patient was advised to maintain a regular exercise routine, practice proper lifting techniques, and return for follow-up if symptoms recur.'''

out=summarizer(conversation1)
print(out)
print("##############")
print(out[0]['summary_text'])