from moviepy.editor import VideoFileClip, concatenate_videoclips

from .step import Step


class EditVideo(Step):
    def process(self, inputs, data, utils):
        clips = []
        count = 0
        limit = inputs['limit']
        for found in data:
            url = found.YT.url
            if not utils.download_video_exist(url):
                continue
            count += 1
            start, end = self.parse_caption_time(found.time)
            print('clip video --- ' + found.caption + '///' + found.time)
            video = VideoFileClip(utils.download_video_path(url)).subclip(t_start=start, t_end=end)
            clips.append(video)
            if count > limit:
                break

        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(utils.download_out_path(inputs))

    def parse_caption_time(self, found_time):
        start, end = found_time.split('-->')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000
